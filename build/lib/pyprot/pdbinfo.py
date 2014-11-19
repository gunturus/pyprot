"""
Sebastian Raschka 2014

Parent class inhereted by Pdb class in pdbmain that contains
methods for compiling and collecting various information about
PDB files.

"""
class PdbInfo(object):
    def __init__():
        pass

    def lookup(self):
        ''' 
        Looks up various information about a PDB file on rcsb.org. 
        Returns a list containing:
        Description, Resolution (A), Method, Title, Ligands (short), Ligands (long) 
        
        '''
        if not self.pdb_code:
            print('Object requires valid .pdb_code attribute')
            return None
        else:
            self.soup = self._lookup_soup()
            self._lookup_resolution()
            self._lookup_title()
            self._lookup_description()
            self._lookup_pdbcontent()
            self._lookup_ligands()
            summary = [self._code, self._desc, self._reso, self._meth, self._ligs, self._titl]
            return summary
        
            
    def lookup_summary(self):
        self.lookup()
        summary = [self._code, self._desc, self._reso, self._meth, self._ligs, self._titl]
        return summary
        
    def _lookup_soup(self):
        url = 'http://www.rcsb.org/pdb/explore/explore.do?structureId=' + self._code
        return bs4.BeautifulSoup(urllib.request.urlopen(url))
    
    def _lookup_pdbcontent(self):
        url = 'http://www.rcsb.org/pdb/files/' + self._code + '.pdb'
        r = urllib.request.urlopen(url)
        self._cont = r.readlines()
    
    def _lookup_resolution(self):
        try:
            reso_tag = self.soup.find('td', {'id': 'se_xrayResolution'})
            resolution = reso_tag.contents[0].strip()
            self._meth = 'X-Ray'
            self._reso = resolution
        except AttributeError:
            self._meth = 'NMR'
            self._reso = '-'
    
    def _lookup_title(self):
        try:
            parent = self.soup.find('div', {'id': 'se_structureTitle'})
            child = parent.find('span', {'class': 'h3'})
            title = child.contents[0]
            self._titl = title
        except AttributeError:
            self._titl = '-'
    
    def _lookup_description(self):
        try:
            desc_tag = self._soup.find('td', {'class': 'mdauData', 'colspan':"99"})
            description = desc_tag.contents[0].strip()
            self._desc = description
        except AttributeError:
            self._desc = '-'      
    
    def _lookup_ligands(self):
        for i in self._cont:
            i = i.decode('utf-8')
            if i.startswith('HETNAM'):
                s = i.split('HETNAM')[1].strip()
                sp = s.split()
                short = sp[0]
                if len(short) == 1:
                    short = sp[1]
                    desc = " ".join(sp[2:])
                else:
                    desc = " ".join(sp[1:])
                
                if short in self.ligs:
                    self._ligs[short] += desc
                else:
                    self._ligs[short] = desc    